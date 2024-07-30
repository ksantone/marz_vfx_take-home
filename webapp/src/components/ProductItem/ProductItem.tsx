import React from 'react';
import { ProductItemProps } from '../interfaces';

const ProductItem: React.FC<ProductItemProps> = ({ product }) => {
  return (
    <div className="p-4 border border-gray-200 rounded-lg shadow-md">
      <img src={product.ProductPhotoURL} alt={product.ProductName} className="w-full h-auto mb-2" />
      <h2 className="text-xl font-bold">{product.ProductName}</h2>
      <p className="text-gray-700">ID: {product.ProductID}</p>
    </div>
  );
};

export default ProductItem;